import { Cloud, Save, Trash2 } from "lucide-react";

import Button from "../../components/ui/Button";

function DesignSystem() {
  return (
    <div className="min-h-screen bg-[var(--color-background)] p-10">
      <h1 className="mb-2 text-3xl font-bold text-[var(--color-text)]">
        CloudSense Design System
      </h1>

      <p className="mb-10 text-[var(--color-text-secondary)]">
        UI Components Preview
      </p>

      {/* Buttons */}

      <section className="space-y-6 rounded-xl border border-[var(--color-border)] bg-[var(--color-surface)] p-8 shadow-sm">
        <h2 className="text-xl font-semibold text-[var(--color-text)]">
          Buttons
        </h2>

        <div className="flex flex-wrap gap-4">
          <Button>Primary</Button>

          <Button variant="secondary">
            Secondary
          </Button>

          <Button variant="danger">
            Delete
          </Button>

          <Button variant="ghost">
            Ghost
          </Button>
        </div>

        <div className="flex flex-wrap gap-4">
          <Button size="sm">
            Small
          </Button>

          <Button>
            Medium
          </Button>

          <Button size="lg">
            Large
          </Button>
        </div>

        <div className="flex flex-wrap gap-4">
          <Button leftIcon={<Cloud size={18} />}>
            Connect AWS
          </Button>

          <Button
            variant="secondary"
            leftIcon={<Save size={18} />}
          >
            Save
          </Button>

          <Button
            variant="danger"
            leftIcon={<Trash2 size={18} />}
          >
            Delete
          </Button>
        </div>

        <div className="flex flex-wrap gap-4">
          <Button loading>
            Saving
          </Button>

          <Button disabled>
            Disabled
          </Button>
        </div>
      </section>
    </div>
  );
}

export default DesignSystem;